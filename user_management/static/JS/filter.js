// Data: Mapping states to districts
const districtData = {
    AP: ["Anantapur", "Chittoor", "East Godavari", "Guntur", "Kadapa", "Krishna", "Kurnool", "Nellore", "Prakasam", "Srikakulam", "Visakhapatnam", "Vizianagaram", "West Godavari"],
    TS: ["Adilabad", "Hyderabad", "Karimnagar", "Khammam", "Mahbubnagar", "Medak", "Nalgonda", "Nizamabad", "Rangareddy", "Warangal"],
    TN: ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli"],
    KA: ["Bengaluru", "Mysuru", "Mangalore", "Hubli", "Belgaum", "Gulbarga"],
    MH: ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur"],
    UP: ["Lucknow", "Kanpur", "Varanasi", "Agra", "Meerut", "Allahabad"],
    DL: ["Central Delhi", "East Delhi", "New Delhi", "North Delhi", "South Delhi", "West Delhi"],
    WB: ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri", "Malda"],
    RJ: ["Jaipur", "Jodhpur", "Udaipur", "Ajmer", "Kota", "Bikaner"],
    MP: ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain", "Sagar"]
};

// Function to load districts based on selected state
function loadDistricts() {
    const stateSelect = document.getElementById('state');
    const districtSelect = document.getElementById('district');
    const selectedState = stateSelect.value;

    // Clear previous options
    districtSelect.innerHTML = '<option value="">Select District</option>';

    if (selectedState && districtData[selectedState]) {
        districtData[selectedState].forEach(function(district) {
            const option = document.createElement('option');
            option.value = district;
            option.textContent = district;
            districtSelect.appendChild(option);
        });
    }
}

// Function to apply filter (you can modify as needed)
function applyFilter() {
    const state = document.getElementById('state').value;
    const district = document.getElementById('district').value;

    if (!state) {
        alert('Please select a state.');
        return;
    }
    if (!district) {
        alert('Please select a district.');
        return;
    }

    // Example Action:
    alert(`Filtering data for State: ${state}, District: ${district}`);

    // ➡️ Here you can also make an AJAX request to Django server if needed.
}
