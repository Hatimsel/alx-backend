const redis = require('redis');


try {
    const client = redis.createClient();
    console.log('Redis client connected to the server');
} catch (err) {
    console.log(`Redis client not connected to the server: ${err}`);
}
