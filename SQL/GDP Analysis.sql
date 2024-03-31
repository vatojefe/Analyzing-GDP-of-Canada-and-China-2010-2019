-- Create a temporary table to store the data
CREATE TEMPORARY TABLE IF NOT EXISTS GDP_Analysis (
    Year INT,
    Canada DECIMAL(18,2),
    China DECIMAL(18,2)
);

-- Insert the provided data into the temporary table
INSERT INTO GDP_Analysis (Year, Canada, China)
VALUES
    (2010, 1666048.00, 7761602.58),
    (2011, 1774063.00, 9198076.81),
    (2012, 1827201.00, 10241758.21),
    (2013, 1902247.00, 11285439.61),
    (2014, 1994898.00, 12329121.01),
    (2015, 1990441.00, 13372802.41),
    (2016, 2025535.00, 14416483.81),
    (2017, 2140641.00, 15460165.21),
    (2018, 2231168.00, 16503846.61),
    (2019, 2310712.00, 17547528.01);

-- Calculate the mean for Canada and China
SELECT 
    AVG(Canada) AS Mean_Canada,
    AVG(China) AS Mean_China
FROM GDP_Analysis;

-- Calculate the mode for Canada and China
SELECT 
    Mode_Canada,
    Mode_China
FROM (
    SELECT 
        Canada AS Mode_Canada,
        ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS rn
    FROM GDP_Analysis
    GROUP BY Canada
    HAVING COUNT(*) >= ALL(SELECT COUNT(*) FROM GDP_Analysis GROUP BY Canada)
) AS subquery1
CROSS JOIN (
    SELECT 
        China AS Mode_China,
        ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS rn
    FROM GDP_Analysis
    GROUP BY China
    HAVING COUNT(*) >= ALL(SELECT COUNT(*) FROM GDP_Analysis GROUP BY China)
) AS subquery2
WHERE subquery1.rn = 1 AND subquery2.rn = 1;

-- Calculate the median for Canada and China
SELECT 
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Canada) AS Median_Canada,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY China) AS Median_China
FROM GDP_Analysis;

-- Calculate the variation for Canada and China
SELECT 
    VARIANCE(Canada) AS Variation_Canada,
    VARIANCE(China) AS Variation_China
FROM GDP_Analysis;

-- Calculate the standard deviation for Canada and China
SELECT 
    STDDEV(Canada) AS StdDev_Canada,
    STDDEV(China) AS StdDev_China
FROM GDP_Analysis;

-- Show data less than the mean for Canada and China
SELECT 
    *
FROM GDP_Analysis
WHERE Canada < (SELECT AVG(Canada) FROM GDP_Analysis)
AND China < (SELECT AVG(China) FROM GDP_Analysis);

-- Show data greater than the mean for Canada and China
SELECT 
    *
FROM GDP_Analysis
WHERE Canada > (SELECT AVG(Canada) FROM GDP_Analysis)
AND China > (SELECT AVG(China) FROM GDP_Analysis);
SELECT * FROM GDP_Analysis;

