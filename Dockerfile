FROM python:3.11.3
WORKDIR /workspace
ADD requirements.txt /workspace/requirements.txt
RUN pip install -r requirements.txt
ADD app.py images/* capynano-model.pkl /workspace/
ENV HOME=/workspace
CMD [ "python3" , "/workspace/app.py" ]