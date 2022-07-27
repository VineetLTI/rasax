FROM rasa/rasa-sdk:3.0.0

COPY actions /app/actions

#RUN PIP install rasa

USER root
#RUN pip install --no-cache-dir -r /app/actions/requirements-actions.txt

USER 1001

CMD ["start", "--actions", "actions"]

