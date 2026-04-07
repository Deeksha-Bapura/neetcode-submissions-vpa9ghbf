class MyHashSet:

    def __init__(self):
        self.num_buckets = 1000
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _hash(self,key: int) -> int:
        return key % self.num_buckets

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)