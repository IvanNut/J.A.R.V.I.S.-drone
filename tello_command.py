from djitellopy import TelloSwarm
import time

# Инициализация дронов
swarm = TelloSwarm.fromIps(['192.168.0.120', '192.168.0.121', '192.168.0.158', '192.168.0.184'])

# Подключение к дронам
swarm.connect()

# Взлет дронов на полметра
swarm.takeoff()
time.sleep(2)  # Ждем, чтобы дроны взлетели

# Подъем на полметра (примерно 50 см)
swarm.move_up(50)

# Ожидание завершения движения
time.sleep(2)

# Приземление дронов
swarm.land()