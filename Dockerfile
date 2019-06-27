# Use a basic Python image
FROM rct.base

# add entrypoint.sh
COPY ./api/entrypoint.sh /rct/entrypoint.sh
RUN chmod +x /rct/entrypoint.sh

EXPOSE 25 465 587

CMD ["/rct/entrypoint.sh"]
