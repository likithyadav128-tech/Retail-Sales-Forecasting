
-- Retail Sales Forecasting SQL Queries
-- Rossmann Store Sales


-- 1. Display all records
SELECT *
FROM sales;

--------------------------------------------------

-- 2. Total number of records
SELECT COUNT(*) AS Total_Records
FROM sales;

--------------------------------------------------

-- 3. Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM sales;

--------------------------------------------------

-- 4. Average Sales
SELECT ROUND(AVG(Sales),2) AS Average_Sales
FROM sales;

--------------------------------------------------

-- 5. Highest Sales
SELECT MAX(Sales) AS Highest_Sales
FROM sales;

--------------------------------------------------

-- 6. Lowest Sales
SELECT MIN(Sales) AS Lowest_Sales
FROM sales;

--------------------------------------------------

-- 7. Total Customers
SELECT SUM(Customers) AS Total_Customers
FROM sales;

--------------------------------------------------

-- 8. Average Customers
SELECT ROUND(AVG(Customers),2) AS Average_Customers
FROM sales;

--------------------------------------------------

-- 9. Sales by Store
SELECT Store,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Store
ORDER BY Total_Sales DESC;

--------------------------------------------------

-- 10. Top 10 Stores by Sales
SELECT Store,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Store
ORDER BY Total_Sales DESC
LIMIT 10;

--------------------------------------------------

-- 11. Bottom 10 Stores
SELECT Store,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Store
ORDER BY Total_Sales ASC
LIMIT 10;

--------------------------------------------------

-- 12. Sales by Day of Week
SELECT DayOfWeek,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY DayOfWeek
ORDER BY DayOfWeek;

--------------------------------------------------

-- 13. Average Sales by Day of Week
SELECT DayOfWeek,
ROUND(AVG(Sales),2) AS Average_Sales
FROM sales
GROUP BY DayOfWeek
ORDER BY DayOfWeek;

--------------------------------------------------

-- 14. Sales by Promotion
SELECT Promo,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Promo;

--------------------------------------------------

-- 15. Average Sales with Promotion
SELECT Promo,
ROUND(AVG(Sales),2) AS Average_Sales
FROM sales
GROUP BY Promo;

--------------------------------------------------

-- 16. Open vs Closed Stores
SELECT Open,
COUNT(*) AS Total_Days
FROM sales
GROUP BY Open;

--------------------------------------------------

-- 17. Sales by Store Type
SELECT StoreType,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY StoreType;

--------------------------------------------------

-- 18. Average Sales by Store Type
SELECT StoreType,
ROUND(AVG(Sales),2) AS Average_Sales
FROM sales
GROUP BY StoreType;

--------------------------------------------------

-- 19. Sales by Assortment
SELECT Assortment,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Assortment;

--------------------------------------------------

-- 20. Sales by School Holiday
SELECT SchoolHoliday,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY SchoolHoliday;

--------------------------------------------------

-- 21. Sales by State Holiday
SELECT StateHoliday,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY StateHoliday;

--------------------------------------------------

-- 22. Sales by Year
SELECT Year,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Year
ORDER BY Year;

--------------------------------------------------

-- 23. Sales by Month
SELECT Month,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Month
ORDER BY Month;

--------------------------------------------------

-- 24. Average Sales by Month
SELECT Month,
ROUND(AVG(Sales),2) AS Average_Sales
FROM sales
GROUP BY Month
ORDER BY Month;

--------------------------------------------------

-- 25. Total Sales by Competition Distance
SELECT
ROUND(CompetitionDistance,-1) AS Competition_Distance,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Competition_Distance
ORDER BY Competition_Distance;

--------------------------------------------------

-- 26. Stores Running Promo2
SELECT Promo2,
COUNT(*) AS Total_Records
FROM sales
GROUP BY Promo2;

--------------------------------------------------

-- 27. Top 20 Highest Sales Days
SELECT Date,
Store,
Sales
FROM sales
ORDER BY Sales DESC
LIMIT 20;

--------------------------------------------------

-- 28. Top 20 Customer Days
SELECT Date,
Store,
Customers
FROM sales
ORDER BY Customers DESC
LIMIT 20;

--------------------------------------------------

-- 29. Average Sales per Store
SELECT Store,
ROUND(AVG(Sales),2) AS Average_Sales
FROM sales
GROUP BY Store
ORDER BY Average_Sales DESC;

--------------------------------------------------

-- 30. Store Performance Summary
SELECT
Store,
SUM(Sales) AS Total_Sales,
SUM(Customers) AS Total_Customers,
ROUND(AVG(Sales),2) AS Average_Sales
FROM sales
GROUP BY Store
ORDER BY Total_Sales DESC;

--------------------------------------------------