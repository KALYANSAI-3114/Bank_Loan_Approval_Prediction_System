#use lightwight python image
FROM python:3.11-slim

#prevent python buffering logs
ENV PYTHONBUFFERED=1

#set working directory 
WORKDIR /app

# copy requirements.txt 

COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy all files

COPY . .

# streamlit port 
EXPOSE 8501

# run streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]


