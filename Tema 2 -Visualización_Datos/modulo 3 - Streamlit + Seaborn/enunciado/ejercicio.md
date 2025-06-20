import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Función para cargar datos
@st.cache_data
def load_data():
    customers = pd.read_csv("data/olist_customers_dataset.csv")
    orders = pd.read_csv("data/olist_orders_dataset.csv")
    order_items = pd.read_csv("data/olist_order_items_dataset.csv")
    payments = pd.read_csv("data/olist_order_payments_dataset.csv")
    reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")
    products = pd.read_csv("data/olist_products_dataset.csv")
    sellers = pd.read_csv("data/olist_sellers_dataset.csv")
    categories = pd.read_csv("data/product_category_name_translation.csv")
    
    # Convertir fechas a datetime
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
    orders["order_approved_at"] = pd.to_datetime(orders["order_approved_at"])
    orders["order_delivered_carrier_date"] = pd.to_datetime(orders["order_delivered_carrier_date"])
    orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])
    orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"])
    
    reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"])
    reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"])

    return customers, orders, order_items, payments, reviews, products, sellers, categories


# --- Funciones para métricas y tablas ---
def clientes_por_estado(customers, orders, fecha_inicio, fecha_fin, top_n=5):
    # Filtrar pedidos por rango de fecha
    pedidos_periodo = orders[(orders["order_purchase_timestamp"] >= fecha_inicio) & (orders["order_purchase_timestamp"] <= fecha_fin)]
    
    # Clientes que han hecho pedidos en ese periodo
    clientes_pedidos = pedidos_periodo["customer_id"].unique()
    
    # Filtrar clientes con pedidos en ese rango
    clientes_activos = customers[customers["customer_id"].isin(clientes_pedidos)]
    
    # Número de clientes por estado
    clientes_estado = clientes_activos.groupby("customer_state").size().reset_index(name="num_clientes")
    
    # Top N estados por clientes
    top_estados = clientes_estado.sort_values("num_clientes", ascending=False).head(top_n)
    
    # Tabla con ciudades y clientes por estado filtrado top
    ciudades = clientes_activos[clientes_activos["customer_state"].isin(top_estados["customer_state"])]
    tabla_ciudades = ciudades.groupby(["customer_state", "customer_city"]).size().reset_index(name="num_clientes")
    
    return top_estados, tabla_ciudades, pedidos_periodo


def pedidos_y_ratios(pedidos_periodo, customers):
    # Número total de pedidos en periodo
    total_pedidos = pedidos_periodo.shape[0]
    
    # Pedidos por estado
    pedidos_estado = pedidos_periodo.groupby("customer_state").size().reset_index(name="num_pedidos")
    
    # Clientes por estado (en total, sin filtrar pedido)
    clientes_estado = customers.groupby("customer_state").size().reset_index(name="num_clientes")
    
    # Unir para calcular porcentaje y ratio pedidos/cliente
    df = pedidos_estado.merge(clientes_estado, on="customer_state", how="left")
    df["porcentaje_pedidos"] = (df["num_pedidos"] / total_pedidos) * 100
    df["ratio_pedidos_cliente"] = df["num_pedidos"] / df["num_clientes"]
    
    return df


def pedidos_tarde_con_diagnostico(orders, customers, fecha_inicio, fecha_fin):
    # Filtrar pedidos en fecha y que tengan fecha de entrega y estimada
    filtro = (orders["order_purchase_timestamp"] >= fecha_inicio) & (orders["order_purchase_timestamp"] <= fecha_fin)
    data = orders.loc[filtro].copy()
    data = data[data["order_delivered_customer_date"].notna() & data["order_estimated_delivery_date"].notna()]
    
    # Calcular días de retraso (positivo si llega tarde)
    data["days_late"] = (data["order_delivered_customer_date"] - data["order_estimated_delivery_date"]).dt.days
    data["tarde"] = data["days_late"] > 0
    
    # Añadir estado y ciudad clientes para análisis
    data = data.merge(customers[["customer_id", "customer_state", "customer_city"]], on="customer_id", how="left")
    
    # Número total pedidos por ciudad en periodo
    total_pedidos_ciudad = data.groupby("customer_city").size().reset_index(name="total_pedidos")
    
    # Pedidos tardíos por ciudad
    pedidos_tarde = data[data["tarde"]]
    tarde_ciudad = pedidos_tarde.groupby("customer_city").agg(
        num_tarde = ("order_id", "count"),
        media_dias_tarde = ("days_late", "mean")
    ).reset_index()
    
    # Unir totales y tardíos para calcular porcentaje
    df = total_pedidos_ciudad.merge(tarde_ciudad, on="customer_city", how="left").fillna(0)
    df["porcentaje_tarde"] = (df["num_tarde"] / df["total_pedidos"]) * 100
    
    # Diagnóstico simple: Si porcentaje_tarde > 30% -> "Problemas de logística", si media_dias_tarde > 5 -> "Retrasos graves"
    condiciones = [
        (df["porcentaje_tarde"] > 30),
        (df["media_dias_tarde"] > 5)
    ]
    opciones = [
        "Problemas de logística",
        "Retrasos graves"
    ]
    df["diagnostico"] = np.select(condiciones, opciones, default="Sin incidencias relevantes")
    
    return df.sort_values("porcentaje_tarde", ascending=False)


def reviews_por_estado(orders, reviews, customers, fecha_inicio, fecha_fin):
    # Filtrar pedidos dentro de fecha
    pedidos_periodo = orders[(orders["order_purchase_timestamp"] >= fecha_inicio) & (orders["order_purchase_timestamp"] <= fecha_fin)]
    
    # Pedidos sin retraso (excluir los tardíos)
    pedidos_no_tarde = pedidos_periodo[
        (pedidos_periodo["order_delivered_customer_date"].notna()) & 
        (pedidos_periodo["order_estimated_delivery_date"].notna()) &
        ((pedidos_periodo["order_delivered_customer_date"] - pedidos_periodo["order_estimated_delivery_date"]).dt.days <= 0)
    ]
    
    # IDs de pedidos sin retraso
    pedidos_ok_ids = pedidos_no_tarde["order_id"].unique()
    
    # Reviews de esos pedidos
    reviews_filtradas = reviews[reviews["order_id"].isin(pedidos_ok_ids)]
    
    # Añadir estado de cliente
    df = reviews_filtradas.merge(customers[["customer_id", "customer_state"]], on="customer_id", how="left")
    
    # Número de reviews y score medio por estado
    resumen = df.groupby("customer_state").agg(
        num_reviews = ("review_id", "count"),
        score_medio = ("review_score", "mean")
    ).reset_index()
    
    return resumen


# --- Streamlit app ---

def main():
    st.title("Dashboard Olist - Análisis de ventas y logística")
    
    customers, orders, order_items, payments, reviews, products, sellers, categories = load_data()
    
    # Filtro de fecha
    min_fecha = orders["order_purchase_timestamp"].min().date()
    max_fecha = orders["order_purchase_timestamp"].max().date()
    fecha_inicio, fecha_fin = st.sidebar.date_input("Rango de fechas (compra):", [min_fecha, max_fecha], min_value=min_fecha, max_value=max_fecha)
    
    if fecha_inicio > fecha_fin:
        st.error("Error: la fecha inicio no puede ser mayor que la fecha fin")
        return
    
    # 1. Clientes por estado y tabla ciudades
    st.header("1. Clientes por estado y ciudades")
    top_estados, tabla_ciudades, pedidos_periodo = clientes_por_estado(customers, orders, pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))
    st.subheader("Top 5 estados por número de clientes")
    st.dataframe(top_estados)
    
    st.subheader("Clientes por ciudad en esos estados")
    st.dataframe(tabla_ciudades)
    
    # 2. Pedidos, porcentaje y ratio pedidos/cliente
    st.header("2. Pedidos por estado y ratios")
    df_pedidos = pedidos_y_ratios(pedidos_periodo, customers)
    st.dataframe(df_pedidos)
    
    st.subheader("Gráfico ratio pedidos/cliente")
    fig1, ax1 = plt.subplots(figsize=(10,5))
    sns.barplot(data=df_pedidos.sort_values("ratio_pedidos_cliente", ascending=False), x="customer_state", y="ratio_pedidos_cliente", ax=ax1)
    ax1.set_ylabel("Ratio pedidos/cliente")
    ax1.set_xlabel("Estado")
    ax1.set_title("Ratio de pedidos medio por cliente por estado")
    st.pyplot(fig1)
    
    st.markdown("""
    **Interpretación:** El ratio indica la frecuencia de compra media por cliente en cada estado. Estados con ratio bajo podrían necesitar campañas para fidelización, mientras que altos indican clientes más recurrentes.
    """)
    
    # 3. Pedidos tardíos y diagnóstico
    st.header("3. Análisis de pedidos tardíos por ciudad")
    df_tarde = pedidos_tarde_con_diagnostico(orders, customers, pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))
    st.dataframe(df_tarde)
    
    st.subheader("Gráfico porcentaje pedidos tardíos")
    fig2, ax2 = plt.subplots(figsize=(12,5))
    sns.barplot(data=df_tarde.head(20), x="customer_city", y="porcentaje_tarde", ax=ax2)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha="right")
    ax2.set_ylabel("% Pedidos tardíos")
    ax2.set_xlabel("Ciudad")
    ax2.set_title("Top 20 ciudades con más porcentaje de pedidos tardíos")
    st.pyplot(fig2)
    
    # 4. Reviews por estado excluyendo pedidos tardíos
    st.header("4. Reviews y puntuaciones promedio por estado (excluyendo pedidos tardíos)")
    resumen_reviews = reviews_por_estado(orders, reviews, customers, pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))
    st.dataframe(resumen_reviews)
    
    st.subheader("Gráfico score medio por estado")
    fig3, ax3 = plt.subplots(figsize=(10,5))
    sns.barplot(data=resumen_reviews.sort_values("score_medio", ascending=False), x="customer_state", y="score_medio", ax=ax3)
    ax3.set_ylabel("Score medio")
    ax3.set_xlabel("Estado")
    ax3.set_title("Score medio de reviews por estado")
    st.pyplot(fig3)
    
    st.markdown("""
    Eliminamos reviews de pedidos tardíos porque su score puede estar sesgado a negativo por la demora.
    """)

if __name__ == "__main__":
    main()
