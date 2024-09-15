FROM nginx

RUN ["rm", "/etc/nginx/conf.d/default.conf"]
COPY uwsgi_params /etc/nginx/conf.d/
RUN ["ln", "-s", "/opt/conf/nginx/default.conf", "/etc/nginx/conf.d/"]