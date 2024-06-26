import redis from 'redis';

const client = redis.createClient();
console.log('Redis client connected to the server');

const schools = {'Portland': 50, 'Seattle': 80, 
                'New York': 20, 'Bogota': 20,
                'Cali': 40, 'Paris': 2};
for (const [key, value] of Object.entries(schools)) {
    client.hset('HolbertonSchools', key, value, redis.print);
}

client.hgetall('HolbertonSchools', (err, obj) => {
    if (err) {
        console.error(`Error occurred: ${err}`);
    } else {
        console.log(obj);
    }
    client.quit();
});
