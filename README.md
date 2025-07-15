# Monitoring Script for file integrity and backup daemon

# Un script care:
# - monitorizează un folder important pasat ca argument in terminal la rularea scriptului monitoring.py,
# - detectează modificări folosing hashing,
# - face backup automat fișierelor redenumite cu timestamp,
# - encodează backupul în Base64 pentru a simula un pas de securitate,
# - mută backupul într-un folder secured/,
# - loghează acțiunile intr-un fisier txt,
# - poate fi pornit periodic cu cron job.
