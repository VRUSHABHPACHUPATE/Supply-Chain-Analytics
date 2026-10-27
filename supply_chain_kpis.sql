-- 1. Total Sales and Order Volume by Product Category
SELECT 
    category_name,
    COUNT(order_item_quantity) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales
FROM cleaned_supply_chain
GROUP BY category_name
ORDER BY total_sales DESC;

-- 2. Late Delivery Rate by Shipping Mode
-- Uses our Python-engineered 'is_delayed' column to evaluate logistics performance
SELECT 
    shipping_mode,
    COUNT(*) AS total_shipments,
    SUM(is_delayed) AS delayed_shipments,
    ROUND((SUM(is_delayed) * 100.0) / COUNT(*), 2) AS late_delivery_rate_pct
FROM cleaned_supply_chain
GROUP BY shipping_mode
ORDER BY late_delivery_rate_pct DESC;

-- 3. High-Risk Regions for Delivery
SELECT 
    order_country,
    COUNT(*) AS total_orders,
    SUM(late_delivery_risk) AS high_risk_orders,
    ROUND((SUM(late_delivery_risk) * 100.0) / COUNT(*), 2) AS risk_percentage
FROM cleaned_supply_chain
GROUP BY order_country
ORDER BY high_risk_orders DESC
LIMIT 10;