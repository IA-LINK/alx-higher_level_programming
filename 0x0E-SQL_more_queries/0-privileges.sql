-- Connect to MySQL as the root user
mysql -h localhost -u root -p
-- Enter your root password when prompted

-- Check privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check privileges for user_0d_2 (optional, comment out if user doesn't exist)
SHOW GRANTS FOR 'user_0d_2'@'localhost';
