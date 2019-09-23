# Use a basic Python image
FROM coffeetrial.base

# add entrypoint.sh
COPY ./api/entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

EXPOSE 25 465 587

CMD ["./entrypoint.sh"]
