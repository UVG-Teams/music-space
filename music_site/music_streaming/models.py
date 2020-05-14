from django.db import models

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