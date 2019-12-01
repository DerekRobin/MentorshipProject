public class Song{

    private String title;
    private String artist;
    private double duration;
    private double tempo;
    private int year; 

    public Song(String title, String artist, double duration, double tempo, int year) {
        this.artist = artist;
        this.duration = duration;
        this.tempo = tempo;
        this.title = title;
        this.year = year;
    }

    public String toString() {
        return "Song [title=" + title + ", artist=" + artist
                + ", duration=" + duration + ", tempo=" + tempo + ", year="
                + year + "] \n";

    }
    
    public String getArtist(){
        return artist;
    }

    public double getDuration(){
        return duration;
    }

    public double getTempo(){
        return tempo;
    }

    public String getTitle(){
        return title;
    }

    public int getYear(){
        return year;
    }

    public void setArtist(){
        this.artist = artist;
    }

    public void setDuration(){
        this.duration = duration;
    }

    public void setTempo(){
        this.tempo = tempo;
    }

    public void setTitle(){
        this.title = title;
    }

    public void setYear(){
        this.year = year;
    }
}