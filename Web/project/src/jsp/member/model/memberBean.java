package jsp.member.model;
 
 
// �������� ������ ����ϴ� Ŭ���� - DTO
public class memberBean 
{
    private String id;            // ���̵�
    private String password;     // ��й�ȣ
    private String name;        // �̸�
    private String phone;        // ��ȭ
    private String device;        // ��ȭ
    
    
    public String getId() {return id;}
    public void setId(String id) {this.id = id;}
    
    public String getPassword() {return password;}
    public void setPassword(String password) {this.password = password;}
    
    public String getName() {return name;}
    public void setName(String name) {this.name = name;}
   
    public String getPhone() {return phone;}
    public void setPhone(String phone) {this.phone = phone;}
    
	public String getDevice() {return device;}
	 public void setDevice(String device) {this.device = device;}
    
}
