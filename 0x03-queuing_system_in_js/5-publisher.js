import redis from 'redis';


const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function publishMessage(message, time) {
    const channel = 'holberton school channel';
    setTimeout(() => {
        client.publish(channel, message, (err, reply) => {
            if (err) {
                console.error(err);
            } else {
                console.log(`About to send ${message}`);
            }
        });
    }, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
