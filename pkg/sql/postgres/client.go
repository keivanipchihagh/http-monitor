package postgres

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

var db *sql.DB

// Checks for errors and panics if any
func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

// Constructs a connection string from the given parameters
func getConnectionInfo(host string, port int, user string, password string, dbname string) string {
	return fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)
}

// Initializes the database connection instance
func Initialize(host string, port int, user string, password string, dbname string) {
	psqlInfo := getConnectionInfo(host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqlInfo)
	checkError(err)

	// Check liveness
	err = db.Ping()
	checkError(err)
}
