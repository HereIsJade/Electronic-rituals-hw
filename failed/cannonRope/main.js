var demo = new CANNON.Demo();
// Sphere chain
demo.addScene("Sphere chain",function(){
  var size = 0.5;
  var dist = size*2+0.12;
  var world = setupWorld(demo);
  //world.solver.setSpookParams(1e20,3);
  var sphereShape = new CANNON.Sphere(size);
  var mass = 1;
  var lastBody = null;
  var N = 20;
  world.solver.iterations = N; // To be able to propagate force throw the chain of N spheres, we need at least N solver iterations.
  for(var i=0; i<N; i++){
    // Create a new body
    var spherebody = new CANNON.Body({ mass: i===0 ? 0 : mass });
    spherebody.addShape(sphereShape);
    spherebody.position.set(10,10,(N-i)*dist);
    spherebody.velocity.x = i;
    world.addBody(spherebody);
    demo.addVisual(spherebody);

    // Connect this body to the last one added
    var c;
    if(lastBody!==null){
      world.addConstraint(c = new CANNON.DistanceConstraint(spherebody,lastBody,dist));
    }

    // Keep track of the lastly added body
    lastBody = spherebody;
  }
});





function setupWorld(demo){
// Create world
var world = demo.getWorld();
world.gravity.set(0,0,-40);
world.broadphase = new CANNON.NaiveBroadphase();
world.solver.iterations = 10;

// ground plane
var groundShape = new CANNON.Plane();
var groundBody = new CANNON.Body({ mass: 0 });
groundBody.addShape(groundShape);
groundBody.position.set(0,0,1);
world.addBody(groundBody);
demo.addVisual(groundBody);

world.quatNormalizeFast = false;
world.quatNormalizeSkip = 0;

return world;
};

demo.start();
