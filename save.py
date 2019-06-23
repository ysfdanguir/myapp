def save(self, outfile, close_file=True, **kwargs):
        """Saves an Element into a file.
        Parameters
        ----------
        outfile : str or file object
            The file (or filename) where you want to output the html.
        close_file : bool, default True
            Whether the file has to be closed after write.
        """
	if isinstance(outfile, text_type) or isinstance(outfile, binary_type):
	    fid = open(outfile, 'wb')
	else:
	    fid = outfile

	root = self.get_root()
	html = root.render(**kwargs)
	fid.write(html.encode('utf8'))
	if close_file:
	    fid.close()

