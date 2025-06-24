import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Datos", layout="wide")
st.title("Dashboard de Datos - Miguel Moreno")

@st.cache_data
def load_data():
    customers = pd.read_csv("data/olist_customers_dataset.csv")
    items = pd.read_csv("data/olist_order_items_dataset.csv")
    payments = pd.read_csv("data/olist_order_payments_dataset.csv")
    reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")
    orders = pd.read_csv("data/olist_orders_dataset.csv")
    products = pd.read_csv("data/olist_products_dataset.csv")
    sellers = pd.read_csv("data/olist_sellers_dataset.csv")
    categories = pd.read_csv("data/product_category_name_translation.csv")
    return customers, items, payments, reviews, orders, products, sellers, categories

customers, items, payments, reviews, orders, products, sellers, categories = load_data()

orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"], errors='coerce')
min_date = orders["order_purchase_timestamp"].min().date()
max_date = orders["order_purchase_timestamp"].max().date()

# Barra lateral para filtros
st.sidebar.header("Filtros")
start_date, end_date = st.sidebar.date_input(
    "Seleccione rango de fechas para filtrar los pedidos",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

mask = (orders["order_purchase_timestamp"].dt.date >= start_date) & \
       (orders["order_purchase_timestamp"].dt.date <= end_date)
orders_filtered = orders.loc[mask].copy()

# Métricas clave
total_orders = orders_filtered["order_id"].nunique()
total_customers = orders_filtered["customer_id"].nunique()

st.sidebar.markdown("---")
st.sidebar.metric("Pedidos en rango", total_orders)
st.sidebar.metric("Clientes únicos", total_customers)

merged = orders_filtered.merge(customers, on="customer_id") \
                        .merge(payments, on="order_id", how="left") \
                        .merge(reviews, on="order_id", how="left") \
                        .merge(items, on="order_id", how="left")

#Sección Clientes
st.header("Clientes por Estado y Ciudad")
top_states = merged["customer_state"].value_counts().nlargest(5).index.tolist()
clientes_estado = merged[merged["customer_state"].isin(top_states)]

clientes_ciudad = clientes_estado.groupby(["customer_state", "customer_city"]).agg(
    num_clientes=("customer_unique_id", "nunique")
).reset_index().sort_values(by="num_clientes", ascending=False)

st.subheader("Clientes por Ciudad")
st.dataframe(clientes_ciudad)


color_base = "#ff9505"
color_secundario = "#ffb347"    
fondo_grafico = "#2c2c2c"
color_texto = "#eeeeee" 

#Gráfico 1 (Clientes por Estado)
fig1, ax1 = plt.subplots(figsize=(10,4))
fig1.patch.set_facecolor(fondo_grafico)
ax1.set_facecolor(fondo_grafico)
sns.countplot(data=clientes_estado, x="customer_state", order=top_states, ax=ax1,
              color=color_base)
ax1.set_xlabel("Estado", color=color_texto)
ax1.set_ylabel("Número de Clientes", color=color_texto)
ax1.set_title("Distribución de Clientes por Estado", color=color_texto)
ax1.tick_params(axis='x', rotation=45, colors=color_texto)
ax1.tick_params(axis='y', colors=color_texto)
for spine in ax1.spines.values():
    spine.set_edgecolor("#555555")
st.pyplot(fig1)

#Sección Pedidos
st.header("Pedidos por Cliente y Estado")

pedidos_por_cliente = merged.groupby("customer_unique_id").agg(
    pedidos=("order_id", "nunique")
).reset_index()

por_estado = merged.groupby("customer_state").agg(
    pedidos=("order_id", "nunique"),
    clientes=("customer_unique_id", "nunique")
).reset_index()

por_estado["pedidos_por_cliente"] = por_estado["pedidos"] / por_estado["clientes"]
por_estado["porcentaje_total"] = 100 * por_estado["pedidos"] / por_estado["pedidos"].sum()

st.subheader("Pedidos por Estado")
st.dataframe(por_estado.sort_values("pedidos", ascending=False))

#Gráfico 2 (Ratio Pedidos por Cliente)
fig2, ax2 = plt.subplots(figsize=(10,5))
fig2.patch.set_facecolor(fondo_grafico)
ax2.set_facecolor(fondo_grafico)
sns.barplot(data=por_estado, x="customer_state", y="pedidos_por_cliente", ax=ax2,
            color=color_secundario)
ax2.set_xlabel("Estado", color=color_texto)
ax2.set_ylabel("Pedidos por Cliente", color=color_texto)
ax2.set_title("Ratio de Pedidos por Cliente", color=color_texto)
ax2.tick_params(axis='x', rotation=45, colors=color_texto)
ax2.tick_params(axis='y', colors=color_texto)
for spine in ax2.spines.values():
    spine.set_edgecolor("#555555")
st.pyplot(fig2)

#Sección Pedidos con retraso
st.header("Pedidos que llegaron tarde")

orders_filtered["order_delivered_customer_date"] = pd.to_datetime(
    orders_filtered["order_delivered_customer_date"], errors='coerce'
)
orders_filtered["order_estimated_delivery_date"] = pd.to_datetime(
    orders_filtered["order_estimated_delivery_date"], errors='coerce'
)

orders_dates = orders_filtered.dropna(
    subset=["order_delivered_customer_date", "order_estimated_delivery_date"]
).copy()

orders_dates["dias_retraso"] = (
    orders_dates["order_delivered_customer_date"] - orders_dates["order_estimated_delivery_date"]
).dt.days

retrasos = orders_dates[orders_dates["dias_retraso"] > 0].merge(customers, on="customer_id")

retrasos_ciudad = retrasos.groupby("customer_city").agg(
    pedidos_retrasados=("order_id", "nunique"),
    media_dias_retraso=("dias_retraso", "mean")
).reset_index().sort_values("pedidos_retrasados", ascending=False)

st.subheader("Pedidos retrasados por Ciudad")
st.dataframe(retrasos_ciudad)

with st.expander("Nota sobre pedidos retrasados"):
    st.markdown(
        "Las ciudades con mayor número de pedidos retrasados suelen tener desafíos logísticos. Se recomienda analizar los transportistas y rutas en estas zonas."
    )

# Sección Valoraciones
st.header("Valoraciones por Estado (excluyendo pedidos con retraso)")

pedidos_retrasados_ids = retrasos["order_id"].unique()
sin_retraso = merged[~merged["order_id"].isin(pedidos_retrasados_ids)]

score_estado = sin_retraso.groupby("customer_state").agg(
    media_score=("review_score", "mean"),
    cantidad_reviews=("review_score", "count")
).reset_index().sort_values("media_score", ascending=False)

st.subheader("Valoraciones promedio por Estado")
st.dataframe(score_estado)

#Gráfico 3 (Valoraciones promedio)
fig3, ax3 = plt.subplots(figsize=(10,4))
fig3.patch.set_facecolor(fondo_grafico)
ax3.set_facecolor(fondo_grafico)
sns.barplot(data=score_estado, x="customer_state", y="media_score", ax=ax3,
            color=color_base)
ax3.set_ylim(1, 5)
ax3.set_xlabel("Estado", color=color_texto)
ax3.set_ylabel("Puntuación media", color=color_texto)
ax3.set_title("Puntuación media de valoraciones sin pedidos retrasados", color=color_texto)
ax3.tick_params(axis='x', rotation=45, colors=color_texto)
ax3.tick_params(axis='y', colors=color_texto)
for spine in ax3.spines.values():
    spine.set_edgecolor("#555555")
st.pyplot(fig3)

st.success("Dashboard cargado correctamente")
