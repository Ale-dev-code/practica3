from config.app import *
from modelos.model import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def GenerateReportVentas(app: App):
    conn = app.bd.getConection()
    query = """
    SELECT
        v.order_id,
        v.product_id,
        v.sales_amount,
        v.quantity,
        s.segment_name,
        m.market_name,
        r.region_name
    FROM
        VENTAS v
    JOIN SEGMENTO s ON v.segment_id = s.id
    JOIN MARKET m ON v.market_id = m.id
    JOIN REGION r ON v.region_id = r.id
    ORDER BY v.sales_amount DESC
    """
    
    df = pd.read_sql_query(query, conn)
    fecha = "08-02"
    path = f"/workspaces/practica3/Proyecto/Controller/report_{fecha}.csv"
    df.to_csv(path, index=False)
    
    # Diseño del reporte con gráficos
    plt.figure(figsize=(10,6))
    sns.barplot(x='segment_name', y='sales_amount', data=df, hue='region_name')
    plt.title('Ventas por Segmento y Región')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"/workspaces/practica3/Proyecto/Controller/report_{fecha}.png")
    
    sendMail(app, path)

def sendMail(app: App, data):
    app.mail.send_email('from@example.com', 'Reporte de Ventas', 'Adjunto el reporte de ventas', data)
