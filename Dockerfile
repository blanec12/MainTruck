# Use an official Python runtime as an image
FROM python:3.10

# The EXPOSE instruction indicates the ports on which a container
EXPOSE 5000

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]
CMD ["run_app.py"]