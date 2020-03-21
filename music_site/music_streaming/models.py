from django.db import models

# Create your models here.

# Artist
class Artist(models.Model):
    artistid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        # managed = False
        db_table = 'artist'

    # def __str__(self):
    #     return self.name

#Album
class Album(models.Model):
    albumid = models.IntegerField(primary_key=True, blank=False, null=False)
    title = models.CharField(max_lenght=30, blank=False, null=False)
    artistid = models.IntegerField(blank=False, null=False)
    artistid = models.ForeignKey("Artist", models.DO_NOTHING, db_column="artistid")

    class Meta:
        db_table = 'artist'

#Employee
class Employee(models.Model):
    employeeid = models.IntegerField(primary_key=True, blank=False, null=False)
    lastname = models.CharField(max_length=20, blank=False, null=False)
    firstname = models.CharField(max_length=20, blank=False, null=False)
    title = models.CharField(max_length=30)
    reportsto = models.IntegerField()
    #TODO: investigar campo date
    # birthdate = models.DateTimeField()
    # hiredate = models.
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    postalcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=24)
    fax = models.CharField(max_length=24)
    email = models.CharField(max_length=60)
    #TODO: Colocar los campos correctos y eliminar el modelo de reportsto arriba
    reportsto = models.ForeignKey("Artist", models.DO_NOTHING, db_column="artistid")

    class Meta:
        db_table = 'employee'
    
#Customer
class Customer(models.Model):
    customerid = models.IntegerField(primary_key=True, blank=False, null=False)
    firstname = models.CharField(max_length=40, blank=False, null=False)
    lastname = models.CharField(max_length=20, blank=False, null=False)
    company = models.CharField(max_length=80)
    address = models.CharField(max_length=70)
    city = models.CharField(max_lenght=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    postalcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=24)
    fax = models.CharField(max_length=24)
    email = models.CharField(max_length=60, blank=False, null=False)
    #TODO: Llave foranea
    supportrepid = models.ForeignKey("Artist", models.DO_NOTHING, db_column="artistid")

        class Meta:
            db_table = 'customer'

#Genre
class Genre(models.Model):
    genreid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=120)

        class Meta:
            db_table = 'genre'


#Invoice
class Invoice(models.Model):
    invoiceid = models.IntegerField(primary_key=True, blank=False, null=False)
    customerid = models.IntegerField(blank=False, null=False)
    #TODO: InvoiceDate TIMESTAMP NOT NULL,
    billingaddress = models.CharField(max_length=70)
    billingcity = models.CharField(max_length=40)
    billingstate = models.CharField(max_length=40)
    billingcountry = models.CharField(max_length=40)
    billingpostalcode = models.CharField(max_length=10)
    #TODO: Total NUMERIC(10,2) NOT NULL,
    #TODO: FOREIGN KEY (CustomerId) REFERENCES Customer (CustomerId) ON DELETE NO ACTION ON UPDATE NO ACTION

        class Meta:
            db_table = 'invoice'

#MediaType
class MediaType(models.Model):
    mediatypeid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=120)

        class Meta:
            db_table = 'mediatype'

#Track
class Track(models.Model):
    trackid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    albumid = models.IntegerField()
    mediatypeid = models.IntegerField(blank=False, null=False)
    genreid = models.IntegerField()
    composer = models.CharField(max_length=220)
    milliseconds = models.IntegerField(blank=False, null=False)
    bytes = models.IntegerField()
    #TODO: UnitPrice NUMERIC(10,2) NOT NULL,
    #TODO: FOREIGN KEY (AlbumId) REFERENCES Album (AlbumId) ON DELETE NO ACTION ON UPDATE NO ACTION,
    #TODO: FOREIGN KEY (GenreId) REFERENCES Genre (GenreId) ON DELETE NO ACTION ON UPDATE NO ACTION,
    #TODO: FOREIGN KEY (MediaTypeId) REFERENCES MediaType (MediaTypeId) ON DELETE NO ACTION ON UPDATE NO ACTION

        class Meta:
            db_table = 'track'

#InvoiceLine
class InvoiceLine(models.Model):
    invoicelineid = models.IntegerField(primary_key=True, blank=False, null=False)
    invoiceid = models.IntegerField(blank=False, null=False)
    trackid = models.IntegerField(blank=False, null=False)
    #TODO: UnitPrice NUMERIC(10,2) NOT NULL,
    quantity = models.IntegerField(blank=False, null=False)
    #TODO: FOREIGN KEY (InvoiceId) REFERENCES Invoice (InvoiceId) ON DELETE NO ACTION ON UPDATE NO ACTION,
    #TODO: FOREIGN KEY (TrackId) REFERENCES Track (TrackId) ON DELETE NO ACTION ON UPDATE NO ACTION

        class Meta:
            db_table = 'invoiceline'

#Playlist
class Playlist(models.Model):
    playlistid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=120)

        class Meta:
            db_table = 'playlist'

#PlaylistTrack
class PlaylistTrack(models.Model):
    playlistid = models.IntegerField(primary_key=True, blank=False, null=False)
    trackid = models.IntegerField(primary_key=True, blank=False, null=False)
    #TODO: FOREIGN KEY (PlaylistId) REFERENCES Playlist (PlaylistId) ON DELETE NO ACTION ON UPDATE NO ACTION,
    #TODO: FOREIGN KEY (TrackId) REFERENCES Track (TrackId) ON DELETE NO ACTION ON UPDATE NO ACTION

    class Meta:
        db_table = 'playlisttrack'


        # Album
        # Employee
        # Customer
        # Genre
        # Invoice
        # MediaType
        # Track
        # InvoiceLine
        # Playlist
        # PlaylistTrack


# /*******************************************************************************
#    Create Primary Key Unique Indexes
# ********************************************************************************/
# DROP INDEX IF EXISTS IFK_AlbumArtistId;
# CREATE INDEX IFK_AlbumArtistId ON Album (ArtistId);
# DROP INDEX IF EXISTS IFK_CustomerSupportRepId;
# CREATE INDEX IFK_CustomerSupportRepId ON Customer (SupportRepId);
# DROP INDEX IF EXISTS IFK_EmployeeReportsTo;
# CREATE INDEX IFK_EmployeeReportsTo ON Employee (ReportsTo);
# DROP INDEX IF EXISTS IFK_InvoiceCustomerId;
# CREATE INDEX IFK_InvoiceCustomerId ON Invoice (CustomerId);
# DROP INDEX IF EXISTS IFK_InvoiceLineInvoiceId;
# CREATE INDEX IFK_InvoiceLineInvoiceId ON InvoiceLine (InvoiceId);
# DROP INDEX IF EXISTS IFK_InvoiceLineTrackId;
# CREATE INDEX IFK_InvoiceLineTrackId ON InvoiceLine (TrackId);
# DROP INDEX IF EXISTS IFK_PlaylistTrackTrackId;
# CREATE INDEX IFK_PlaylistTrackTrackId ON PlaylistTrack (TrackId);
# DROP INDEX IF EXISTS IFK_TrackAlbumId;
# CREATE INDEX IFK_TrackAlbumId ON Track (AlbumId);
# DROP INDEX IF EXISTS IFK_TrackGenreId;
# CREATE INDEX IFK_TrackGenreId ON Track (GenreId);
# DROP INDEX IF EXISTS IFK_TrackMediaTypeId;
# CREATE INDEX IFK_TrackMediaTypeId ON Track (MediaTypeId);



        # CREATE TABLE Album
        #     AlbumId INT NOT NULL,
        #     Title VARCHAR(160) NOT NULL,
        #     ArtistId INT NOT NULL,
        #     CONSTRAINT PK_Album PRIMARY KEY (AlbumId),
        #     FOREIGN KEY (ArtistId) REFERENCES Artist (ArtistId) ON DELETE NO ACTION ON UPDATE NO ACTION

        # CREATE TABLE Employee
        #     EmployeeId INT NOT NULL,
        #     LastName VARCHAR(20) NOT NULL,
        #     FirstName VARCHAR(20) NOT NULL,
        #     Title VARCHAR(30),
        #     ReportsTo INT,
        #     BirthDate TIMESTAMP,
        #     HireDate TIMESTAMP,
        #     Address VARCHAR(70),
        #     City VARCHAR(40),
        #     State VARCHAR(40),
        #     Country VARCHAR(40),
        #     PostalCode VARCHAR(10),
        #     Phone VARCHAR(24),
        #     Fax VARCHAR(24),
        #     Email VARCHAR(60),
        #     CONSTRAINT PK_Employee PRIMARY KEY (EmployeeId),
        #     FOREIGN KEY (ReportsTo) REFERENCES Employee (EmployeeId) ON DELETE NO ACTION ON UPDATE NO ACTION

        # CREATE TABLE Customer
        #     CustomerId INT NOT NULL,
        #     FirstName VARCHAR(40) NOT NULL,
        #     LastName VARCHAR(20) NOT NULL,
        #     Company VARCHAR(80),
        #     Address VARCHAR(70),
        #     City VARCHAR(40),
        #     State VARCHAR(40),
        #     Country VARCHAR(40),
        #     PostalCode VARCHAR(10),
        #     Phone VARCHAR(24),
        #     Fax VARCHAR(24),
        #     Email VARCHAR(60) NOT NULL,
        #     SupportRepId INT,
        #     CONSTRAINT PK_Customer PRIMARY KEY (CustomerId),
        #     FOREIGN KEY (SupportRepId) REFERENCES Employee (EmployeeId) ON DELETE NO ACTION ON UPDATE NO ACTION

        # CREATE TABLE Genre
        #     GenreId INT NOT NULL,
        #     Name VARCHAR(120),
        #     CONSTRAINT PK_Genre PRIMARY KEY (GenreId)

        # CREATE TABLE Invoice
        #     InvoiceId INT NOT NULL,
        #     CustomerId INT NOT NULL,
        #     InvoiceDate TIMESTAMP NOT NULL,
        #     BillingAddress VARCHAR(70),
        #     BillingCity VARCHAR(40),
        #     BillingState VARCHAR(40),
        #     BillingCountry VARCHAR(40),
        #     BillingPostalCode VARCHAR(10),
        #     Total NUMERIC(10,2) NOT NULL,
        #     CONSTRAINT PK_Invoice PRIMARY KEY (InvoiceId),
        #     FOREIGN KEY (CustomerId) REFERENCES Customer (CustomerId) ON DELETE NO ACTION ON UPDATE NO ACTION

        # CREATE TABLE MediaType
        #     MediaTypeId INT NOT NULL,
        #     Name VARCHAR(120),
        #     CONSTRAINT PK_MediaType PRIMARY KEY (MediaTypeId)

        # CREATE TABLE Track
        #     TrackId INT NOT NULL,
        #     Name VARCHAR(200) NOT NULL,
        #     AlbumId INT,
        #     MediaTypeId INT NOT NULL,
        #     GenreId INT,
        #     Composer VARCHAR(220),
        #     Milliseconds INT NOT NULL,
        #     Bytes INT,
        #     UnitPrice NUMERIC(10,2) NOT NULL,
        #     CONSTRAINT PK_Track PRIMARY KEY (TrackId),
        #     FOREIGN KEY (AlbumId) REFERENCES Album (AlbumId) ON DELETE NO ACTION ON UPDATE NO ACTION,
        #     FOREIGN KEY (GenreId) REFERENCES Genre (GenreId) ON DELETE NO ACTION ON UPDATE NO ACTION,
        #     FOREIGN KEY (MediaTypeId) REFERENCES MediaType (MediaTypeId) ON DELETE NO ACTION ON UPDATE NO ACTION

        # CREATE TABLE InvoiceLine
        #     InvoiceLineId INT NOT NULL,
        #     InvoiceId INT NOT NULL,
        #     TrackId INT NOT NULL,
        #     UnitPrice NUMERIC(10,2) NOT NULL,
        #     Quantity INT NOT NULL,
        #     CONSTRAINT PK_InvoiceLine PRIMARY KEY (InvoiceLineId),
        #     FOREIGN KEY (InvoiceId) REFERENCES Invoice (InvoiceId) ON DELETE NO ACTION ON UPDATE NO ACTION,
        #     FOREIGN KEY (TrackId) REFERENCES Track (TrackId) ON DELETE NO ACTION ON UPDATE NO ACTION

        # CREATE TABLE Playlist
        #     PlaylistId INT NOT NULL,
        #     Name VARCHAR(120),
        #     CONSTRAINT PK_Playlist PRIMARY KEY (PlaylistId)

        # CREATE TABLE PlaylistTrack
        #     PlaylistId INT NOT NULL,
        #     TrackId INT NOT NULL,
        #     CONSTRAINT PK_PlaylistTrack PRIMARY KEY (PlaylistId, TrackId),
        #     FOREIGN KEY (PlaylistId) REFERENCES Playlist (PlaylistId) ON DELETE NO ACTION ON UPDATE NO ACTION,
        #     FOREIGN KEY (TrackId) REFERENCES Track (TrackId) ON DELETE NO ACTION ON UPDATE NO ACTION