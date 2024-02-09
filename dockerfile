# Bu Docker dosyası, PostgreSQL tablosunu oluşturmak için kullanılan Python betiğini içerir.

# Resmi Python görüntüsünü kullan
FROM python:3.7

# Çalışma dizini /app olarak ayarla
WORKDIR /app

# Gerekli Python paketlerini yükle
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Docker konteyneri başlatıldığında çalışacak komut
CMD ["python", "create-table.py"]
