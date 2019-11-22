import com.microsoft.azure.documentdb.ConnectionPolicy;
import com.microsoft.azure.documentdb.ConsistencyLevel;
import com.microsoft.azure.documentdb.Document;
import com.microsoft.azure.documentdb.DocumentClient;
import com.microsoft.azure.documentdb.DocumentClientException;
import com.microsoft.azure.documentdb.FeedResponse;
import com.microsoft.azure.documentdb.RequestOptions;
import Family;


public class Test {

	private static final String HOST = "";
	private static final String MASTER_KEY = "";

	public static DocumentClient client = new DocumentClient(HOST, MASTER_KEY, ConnectionPolicy.GetDefault(),
			ConsistencyLevel.Session);

	public static Family andersenFamily = new Family();

	public void TestCreateDocument() throws DocumentClientException {
		// Insert your Java objects as documents
		System.out.println("Creating doc");

		andersenFamily.setId("Andersen.1");
		andersenFamily.setLastName("Andersen");

		this.client.createDocument("/dbs/familydb/colls/familycoll", andersenFamily, new RequestOptions(), true);

		System.out.println("Done Creating doc");
	}

	public void TestQueryDocuments() {

		System.out.println("Querying db...");
		FeedResponse<Document> queryResults = this.client.queryDocuments("/dbs/familydb/colls/familycoll",
				"SELECT * FROM Family WHERE Family.id = 'Andersen.1'", null);

		System.out.println("Running SQL query...");
		for (Document family : queryResults.getQueryIterable()) {
			System.out.println(String.format("\tRead %s", family));
		}

	}

	public void TestReplaceDocument() throws DocumentClientException {
		// Update a property
		andersenFamily.setLastName("Petersons");
		this.client.replaceDocument("/dbs/familydb/colls/familycoll/docs/Andersen.1", andersenFamily, null);
	}
	
	public void TestReplaceDocument_doc_obj_passed() throws DocumentClientException {
		// Update a property
		Document rFamily =new Document();
		this.client.replaceDocument(rFamily, null);
	}

	public void TestDeleteDocument() throws DocumentClientException {
		this.client.deleteDocument("", null);
	}
	
	public void TestReadDocument() throws DocumentClientException {
		this.client.readDocument("/dbs/familydb/colls/familycoll/docs/Andersen.1", null);
	}
	public void TestReadDocuments() throws DocumentClientException {
		this.client.readDocuments("/dbs/familydb", null);
	}
	

	public static void main(String[] args) throws DocumentClientException {
		Test p = new Test();
		// p.TestCreateDocument();
		p.TestQueryDocuments();
	}

}
