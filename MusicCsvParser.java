import java.util.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.apache.commons.csv.*;

public class MusicCsvParser {

    //file name
    private static final String CSV_FILE_PATH = "./test.csv";
    //CSV file header
    private static final String[] FILE_HEADER_MAPPING = {"artist.name", "duration", "tempo", "title", "year"};

    //Song Attributes
    private static final String SONG_TITLE = "title";
    private static final String SONG_ARTIST = "artist.name";
    private static final String SONG_DUARITON = "duration";
    private static final String SONG_TEMPO = "tempo";
    private static final String SONG_YEAR = "year"; 

    public static ArrayList<Song> readCSV() throws IOException {
        
        //init file reader and csv file parser
        FileReader reader = new FileReader(CSV_FILE_PATH);
        CSVParser parser = CSVParser.parse(reader, CSVFormat.EXCEL.withHeader("artist.name", "duration", "tempo", "title", "year"));

        //Create null list of songs to populate
        ArrayList<Song> songs = new ArrayList<Song>();

        //Get a list of CSV file records
        List<CSVRecord> csvRecords = parser.getRecords(); 


        for (int i = 1; i < csvRecords.size(); i++) {
            CSVRecord record = csvRecords.get(i);
            Song song = new Song(record.get(SONG_TITLE), record.get(SONG_ARTIST), Double.parseDouble(record.get(SONG_DUARITON)), Double.parseDouble(record.get(SONG_TEMPO)),
            Integer.parseInt(record.get(SONG_YEAR)));
            songs.add(song);
        }

        return songs; 

    }


    public static String getSongInfo(ArrayList<Song> songsToSearch, String desiredSong) {

        String songToReturn = null;

        for(Song songToCheck : songsToSearch) {
            if(songToCheck.getTitle().equals(desiredSong)){
                songToReturn = songToCheck.toString();
            }
        }

        return songToReturn;

    }

    public static ArrayList<Song> getAllSongsByYear(ArrayList<Song> songsToSearch, int desiredYear) {

        ArrayList<Song> songsByYear = new ArrayList<Song>();

        for(Song songToCheck : songsToSearch) {
            if(songToCheck.getYear() == desiredYear) {
                songsByYear.add(songToCheck);
            }
        }

        return songsByYear;

    }

    public static void main(String[] args) throws IOException {
        System.out.println(readCSV().toString());

        System.out.println("\nAll song info on \"Soul Deep\"");
        System.out.println(getSongInfo(readCSV(), "Soul Deep"));

        System.out.println("\nAll songs with year == 0");
        System.out.println(getAllSongsByYear(readCSV(), 0).toString());
    }

}


