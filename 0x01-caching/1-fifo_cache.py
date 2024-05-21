#!/usr/bin/python3
"""FIFO Cache Replacement Implementation Class
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    An implementation of FIFO(First In Fisrt Out) Cache

    Attributes:
        __keys (list): Stores cache keys in order of entry using `.append`
        __rlock (RLock): Lock accessed resources to prevent race condition
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """ Get an item by key
        """
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _balance(self, keyIn):
        """ Removes the oldest item from the cache at MAX size
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__keys:
                keysLength = len(self.__keys)
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(0)
                    self.cache_data.pop(keyOut)
                self.__keys.insert(keysLength, keyIn)
        return keyOut
