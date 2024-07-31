import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.exit();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs for each item in the jobs array', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Your verification code is 1234' },
      { phoneNumber: '0987654321', message: 'Your verification code is 4321' }
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
  });


  it('should log the correct messages when jobs are created', () => {
    const jobs = [
       { phoneNUmber: '1234567890', message: 'Your verification code is 1234' }
    ];

    const consoleSpy = [];
    const log = console.log;
    console.log = (msg) => consoleSpy.push(msg);

    createPushNotificationsJobs(jobs, queue);

    expect(consoleSpy[0]).to.match(/Notification job created: \d+/);
    console.log = log;
  });


  it('should properly handle job completion', (done) => {
    const jobs = [
      { phoneNumber: '0123456789', message: 'Your verification code is 1234'}
    ];

    createPushNotificationsJobs(jobs, queue);
    queue.testMode.jobs[0].on('complete', () => {
      expect(true).to.be.true;
      done();
    });

    queue.testMode.jobs[0].emit('complete');
  });


  it('should properly handle job failure', (done) => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Your verification code is 1234' }
    ];

    createPushNotificationsJobs(jobs, queue);
    queue.testMode.jobs[0].on('failed', (err) => {
      expect(err).to.equal('some error');
      done();
    });

    queu.testMode.jobs[0].emit('failed', 'some error');
  });


  it('should properly handle job progress', (done) => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Your verification code is 1234' }
    ];

    createPushNotificationsJobs(jobs, queue);
    queue.testMode.jobs[0].on('progress', (progress) => {
      expect(progress).to.equal(50);
      done();
    });

    queue.testMode.jobs[0].emit('progress', 50);
  });
});
