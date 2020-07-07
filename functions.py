import math

hashrate = int(input("\n Hashrate (TH/s): "))
power_usage = float(input("\n Power Usage: "))
difficulty = int(input("\n Difficulty: "))
electricity_rate = float(input("\n Electricity Rate (kWh): $"))
block_reward = float(input("\n Block Reward: "))
fee_percentage = float(input("\n Fee Percentage: "))

# function for calculating cost

def production_cost():

    full_rewards = (fee_percentage * block_reward) + block_reward
    network_hashrate = difficulty/135500
    efficiency = power_usage/hashrate
    network_power_usage = efficiency * network_hashrate

    production_cost_value = round((((network_power_usage / 6000) * electricity_rate)/full_rewards), 2)

    print(f"\n Production Cost: ${production_cost_value} USD per coin")

def recovery_time():


production_cost()
