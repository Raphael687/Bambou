var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 500 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var player;
var ennemy;
var bg;
var platforms;
var cursors;
var keySpace;

var game = new Phaser.Game(config);

function preload ()
{
    
}