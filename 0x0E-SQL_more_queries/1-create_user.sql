# Connect to MySQL as the root user
mysql -h localhost -u root -p

# Enter your root password when prompted

# Create user user_0d_1 with password, handling potential duplicate error
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

# Grant all privileges on all databases to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

# Flush privileges to ensure immediate effect
FLUSH PRIVILEGES;

# Exit MySQL
quit;
