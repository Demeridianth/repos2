const GREETINGS = ['Hello world', 'All hands on deck', 'Hello there!',];

module.exports = async (req, res) => {
    res.send({
        greeting: GREETINGS[ Math.floor( Math.random() * GREETINGS.length )]
    });
};
