// https://github.com/naomiaro/waveform-playlist
var playlist = WaveformPlaylist.init({
    samplesPerPixel: 1600,
    waveHeight: 120,
    container: document.getElementById('playlist'),
    timescale: true,
    state: 'cursor',
    colors: {
        waveOutlineColor: '#E0EFF1'
    },
    controls: {
        show: true,
        width: 200
    },
    isAutomaticScroll: true,
    zoomLevels: [500, 1000, 1600, 3000, 5000],
    exclSolo: true //enabling exclusive solo
});

var activatedEntry;

// Add listener to a given link
function addEntryListener(link) {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        
        document.getElementById("video_area").style.display = "none";
        document.getElementById("my_video").innerHTML = "";
        
        // Toggle entry highlight
        activatedEntry.classList.remove('active');
        activatedEntry = link;
        activatedEntry.classList.add('active');        
        $(playlist.rootNode).fadeTo('fast', 0,function() {
            playlist.clear();

            // Load mixed track
            playlist.load([
                {
                    'src': link.href + '_mix.wav',
                    'name': 'Mix',
                    'soloed': true,
                },
                {
                    'src': link.href + '_acc.wav',
                    'name': 'Acc'
                },
                {
                    'src': link.href + '_vocA.wav',
                    'name': 'Vocal A'
                },
                {
                    'src': link.href + '_vocB.wav',
                    'name': 'Vocal B'
                }
            ]).then(function () {
                $(playlist.rootNode).fadeTo('fast', 1);
            });
            build_download_block(link.href)

        });        
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', function () {
    links = document.querySelectorAll('#playlist a');
    // Add listeners for default songs
    Array.prototype.forEach.call(links, function (link, index) {
        addEntryListener(link);
    });
    // Load the first track
    activatedEntry = document.querySelectorAll('#playlist a')[0];
    activatedEntry.click();
});

function build_download_block(link_href){
    $('#download_mix').attr('href', link_href + '_mix.wav');
    $('#download_acc').attr('href', link_href + '_acc.wav');
    $('#download_vocA').attr('href', link_href + '_vocA.wav');
    $('#download_vocB').attr('href', link_href + '_vocB.wav');
}