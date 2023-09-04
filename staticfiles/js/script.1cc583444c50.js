$(document).ready(function () {
  $("#id_create").on("click", function () {
    console.log("Create on click...");

    $name = $("id_name").val();
    $district = $("id_district").val();
    $type = $("id_type").val();
    $address = $("id_address").val();
    $lat = $("id_lat").val();
    $lng = $("id_lng").val();
    $timeOpen = $("id_timeOpen").val();
    $timeClose = $("id_timeClose").val();
    $website = $("id_website").val();
    $vr = $("id_vr").val();
    $pic1 = $("id_pic1").val();
    $pic2 = $("id_pic2").val();
    $pic3 = $("id_pic3").val();
    $detail = $("id_detail").val();
    $place_user = $("id_place_user").val();

    // if ($name == "") {
    //   alert("กรุณาป้อนชื่อกิจการ!");
    //   return;
    // }
    // if ($address == "") {
    //   alert("กรุณาป้อนที่อยู่!");
    //   return;
    // }
    // if ($lat == "") {
    //   alert("กรุณาป้อนที่อยู่ ละทิจูด!");
    //   return;
    // }
    // if ($lng == "") {
    //   alert("กรุณาป้อนที่อยู่ ลองทิจูด!");
    //   return;
    // }
    // if ($pic1 == "") {
    //   alert("กรุณาเพิ่มรูปภาพหลัก!");
    //   return;
    // }
    // if ($pic2 == "") {
    //   alert("กรุณาเพิ่มรูปภาพรอง1!");
    //   return;
    // }
    // if ($pic3 == "") {
    //   alert("กรุณาเพิ่มรูปภาพรอง2!");
    //   return;
    // }
    // if ($place_use == "") {
    //   alert("กรุณาเพิ่มรหัสผู้ใช้!");
    //   return;
    // }

  });
});

function Read() {
    alert("Show Table");a
}
