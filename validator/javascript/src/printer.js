class Printer {

  static error(message) {
    const dataReturn = {'status': 'error', message };
    console.log(JSON.stringify(dataReturn));
    process.exit(0);
  }

  static success(result) {
    const dataReturn = {'status': 'success', result };
    console.log(JSON.stringify(dataReturn));
    process.exit(0);
  }
}

module.exports = {
  Printer
}