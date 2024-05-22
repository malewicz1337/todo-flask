FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=todo_db
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

COPY ./init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

CMD ["mysqld"]
