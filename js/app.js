Parse.initialize("NR17YzLLSdbUtQgdtr0WTSHOobI750DpK5t41fEF", "Eb2FWgOYHfaORrl7JaUqSe2kLGljuF3SUVWZZlEg");

var name_palace = [];
var name_palace_html = '';
var current_room_index = 0;
var room_index = 0;

$('#add_memory').hide();
$('#name_palace').hide();
$('#add_someone').hide();

$('#add_room_form').submit(function(event){
  event.preventDefault();
  if( $('#room_name').val() ) {
    var room = $('#room_name').val();

    // Reset input to blank
    $('#room_name').val('');

    // Add the room name to the array
    name_palace.push([room,'','','']);

    // Add the room name to Parse
    var Memory = Parse.Object.extend("Memory");
    var memory = new Memory();

    memory.set("room", room);
    memory.save(null, {
      success: function(memory) {
        // Execute any logic that should take place after the object is saved.
        alert('Created Object ID: ' + memory.id);
      },
      error: function(memory, error) {
        // Execute any logic that should take place if the save fails.
        // error is a Parse.Error with an error code and description.
        alert('Failed to create new object, with error code: ' + error.message);
      }
    });

    var query = new Parse.Query(Memory);
    query.get(objectId, {
      success: function(memory) {
        // The object was retrieved successfully.
        // do something with it
        name_palace[room_index][3] = objectId;
      },
      error: function(object, error) {
        // The object was not retrieved successfully.
        // warn the user
      }
    });



    // Build the ordered list of rooms in this format
    /*
    <li>
      <ul id="memory0">
        <li>Room: Dining Room</li>
        <li>Name: Ryan Carson</li>
        <li>Action: Roller skating</li>
      </ul>
    </li>
    <li>
      <ul class="memory1">
        <li>Room: Kitchen</li>
        <li>Name: Marta Carson</li>
        <li>Action: Munching moles</li>
      </ul>
    </li>
    */

    // If added Memories already, just add the new <li>
    if(name_palace[0][1] != "") {
      name_palace_html = '<li><ul id="memory'+room_index+'"><li>Room: ' + room + '</li></ul></li>';
      $('#name_palace').append(name_palace_html);
    } else {
      name_palace_html += '<li><ul id="memory'+room_index+'"><li>Room: ' + room + '</li></ul></li>';
      $('#name_palace').html(name_palace_html);
    }
    room_index++;
    $('#name_palace').show();

    // If there are more rooms to cycle through, show the add link again
    if(name_palace.length > 0) {
      $('#add_someone').show();
    }
  }
});

$('#done').click(function(event){
  event.preventDefault();
  $('#add_room_form').hide();
});

// Show the Add a Person form with the room name
$('#add_someone').click(function(event){
  event.preventDefault();
  $('#room').html(name_palace[current_room_index][0]);
  $('#add_memory').show();
});

$('#add_memory_form').submit(function(event){
  event.preventDefault();

  if( $('#person_name').val() && $('#person_action').val()) {
    // Add the person's name and action to the room
    name_palace[current_room_index][1] = $('#person_name').val();
    name_palace[current_room_index][2] = $('#person_action').val();

    // Save the data to Parse
    var objectID = name_palace[current_room_index][3];
    console.log("ObjectID: "+objectID);

    var Memory = Parse.Object.extend("Memory");
    var query = new Parse.Query(Memory);
    query.get(objectID, {
      success: function(memory) {
        // The object was retrieved successfully.
        console.log("Updated stuff");
        memory.set("person_name", $('#person_name').val());
        memory.set("action", $('#person_action').val());
        memory.save(null, {
          success: function(memory) {
            // Execute any logic that should take place after the object is saved.
            alert('New object created with objectId: ' + memory.id);
          },
          error: function(memory, error) {
            // Execute any logic that should take place if the save fails.
            // error is a Parse.Error with an error code and description.
            alert('Failed to create new object, with error code: ' + error.message);
          }
        });
      },
      error: function(object, error) {
        // The object was not retrieved successfully.
        // error is a Parse.Error with an error code and description.
        console.log("Error retrieving data: "+error);
      }
    });

    // Update the ordered list
    $('#memory'+current_room_index).append('<li>Name: '+$('#person_name').val()+'</li><li>Action: '+$('#person_action').val()+'</li>');

    current_room_index++;

    // Reset the inputs to blank
    $('#person_name').val('').focus();
    $('#person_action').val('');

    // If there are still available rooms, show the next room name
    if (name_palace.length > current_room_index) {
      $('#room').text(name_palace[current_room_index][0]);
    }
  }
});
