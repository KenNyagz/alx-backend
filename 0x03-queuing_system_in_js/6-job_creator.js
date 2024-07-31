import kue from 'kue';
 
const queue = kue.createQueue();

const jobData = {
  phoneNo: '1234567890',
  message: 'Your verification code is 1234'
}

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Failed to create job:', err);
    }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.error('Notification job failed:', err);
});

