FROM python:3.10-slim

WORKDIR /app
COPY . /app
COPY Model/best_model.pth /app/Model/best_model.pth

# RUN apt update && apt install -y htop python3-dev python3-pip python3-venv

# RUN python3 -m venv venv
# RUN . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# CMD . venv/bin/activate && python3 manage.py runserver 0.0.0.0:8000
CMD python manage.py runserver 0.0.0.0:8000