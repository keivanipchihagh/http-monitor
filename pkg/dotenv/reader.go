package dotenv

import (
	"log"
	"os"
	"regexp"
	"strconv"

	"github.com/joho/godotenv"
)

func checkErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

// Loads the .env file from the root of the project
func LoadEnv() {
	re := regexp.MustCompile(`^(.*` + "http-monitor" + `)`)
	cwd, _ := os.Getwd()
	rootPath := re.Find([]byte(cwd))

	err := godotenv.Load(string(rootPath) + `/.env`)
	checkErr(err)
}

// Reads the value of the given key from the .env file
func ReadEnv(key string) string {
	value := os.Getenv(key)
	if value == "" {
		log.Fatalf("Cannot find '%s' in .env file", key)
	}
	return value
}

// Reads the value of the given key from the .env file and returns it as integer
func ReadEnvAsInt(key string) int {
	value, err := strconv.Atoi(ReadEnv(key))
	checkErr(err)
	return value
}
