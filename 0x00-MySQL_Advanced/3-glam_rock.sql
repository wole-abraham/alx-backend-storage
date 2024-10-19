-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT 
    band_name, 
    CASE 
        WHEN split IS NULL THEN 2022 - formed  -- If the band is still active, calculate lifespan until 2022
        ELSE split - formed                   -- If the band has split, calculate lifespan until the split year
    END AS lifespan
FROM 
    metal_bands;
