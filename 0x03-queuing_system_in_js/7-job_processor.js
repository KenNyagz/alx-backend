import kue from 'kue';

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Initialize progress to 0%

  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    return done(new Error(errorMessage)); // Fail job if no. blacklisted
  }

  job.progress(50, 100); // Tack job progress to 50% 
  console.log(`Sending notificaation to ${phoneNumber}, with message: ${message}`);
  done(); // Complete job after simulating sending a notification
}

// Process jobs from the queue "push_notification_code)2"
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
