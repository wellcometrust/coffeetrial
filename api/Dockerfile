# Use a basic Python image
FROM rct.base

# add entrypoint.sh
COPY ./entrypoint.sh /rct/entrypoint.sh
RUN chmod +x /rct/entrypoint.sh

CMD ["/rct/entrypoint.sh"]
