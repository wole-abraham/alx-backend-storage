-- Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.

-- Create an index on the first letter of the 'name' column
CREATE INDEX idx_name_first ON names (SUBSTRING(name, 1, 1));

