import hazelcast

client = hazelcast.HazelcastClient(cluster_name="my-cluster")
distributed_map = client.get_map("my-distributed-map").blocking()

key = "1"
distributed_map.put(key, 0)

for i in range(1000):
    value = distributed_map.get(key)
    value += 1
    distributed_map.put(key, value)

client.shutdown()