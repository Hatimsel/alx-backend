import kue from 'kue';
import redis from 'redis';

const redisClient = redis.createClient();

const queue = kue.createQueue({
    redis: {
        createClientFactory: () => redisClient
    }
});

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});

queue.on('ready', () => {
    console.log('Worker is ready and listening for jobs...');
});

queue.on('error', (err) => {
    console.error('Queue error:', err);
});
