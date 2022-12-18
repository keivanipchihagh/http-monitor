package store

import (
	"fmt"
	"time"

	"github.com/go-redis/redis"
)

var cache *redis.Client

// Note that in a real world usage, the cache duration shouldn't have
// an expiration time, an LRU policy config should be set where the
// values that are retrieved less often are purged automatically from
// the cache and stored back in RDBMS whenever the cache is full
const CacheDuration = 6 * time.Hour

// Checks for errors and panics if any
func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

// Initializes the cache connection instance
func Initialize(host string, port string, password string, dbname int) {
	cache := redis.NewClient(&redis.Options{
		Addr:     fmt.Sprintf("%s:%s", host, port),
		Password: password,
		DB:       dbname,
	})

	// Check liveness
	_, err := cache.Ping().Result()
	checkError(err)
}
