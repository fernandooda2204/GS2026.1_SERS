import random
import time

class SpaceEnergyMonitor:
    def __init__(self):
        self.solar_panels_kw = 5.0
        self.battery_level = 100.0
        self.consumption_kw = 2.0
        self.is_running = True

    def update_systems(self):
        # Simula flutuações
        self.solar_panels_kw = max(
            0,
            self.solar_panels_kw + random.uniform(-0.5, 0.5)
        )

        self.consumption_kw = max(
            0.5,
            self.consumption_kw + random.uniform(-0.2, 0.2)
        )

        # Atualiza bateria: (Geração - Consumo)
        net_energy = self.solar_panels_kw - self.consumption_kw

        self.battery_level = max(
            0,
            min(100, self.battery_level + net_energy * 0.1)
        )

    def display_status(self):
        print("\n--- STATUS DA MISSÃO ESPACIAL ---")
        print(f"Geração Solar: {self.solar_panels_kw:.2f} kW")
        print(f"Consumo Atual: {self.consumption_kw:.2f} kW")
        print(f"Nível da Bateria: {self.battery_level:.2f}%")

        if self.battery_level < 20:
            print("!!! ALERTA: Nível de bateria crítico! Reduzindo consumo...")

        if self.solar_panels_kw < 0.5:
            print("!!! ALERTA: Baixa incidência solar detectada.")

    def run(self):
        while self.is_running:
            print("\n1. Monitorar Sistemas")
            print("2. Sair")

            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.update_systems()
                self.display_status()

            elif choice == '2':
                self.is_running = False
                print("Encerrando monitoramento...")

            else:
                print("Opção inválida.")

if __name__ == "__main__":
    monitor = SpaceEnergyMonitor()
    monitor.run()