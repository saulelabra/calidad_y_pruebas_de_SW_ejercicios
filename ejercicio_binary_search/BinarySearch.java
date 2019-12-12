public class BinarySearch  {
    
    public static void main (String[] args){
        int[] a = new int[50];
        
        for(int i=0;i<a.length;i++){
            a[i]=i;
        }
        
        System.out.println(binarySearch(a,a[a.length-1]));
    }
	
	
	public static int binarySearch(int[] array,int lookingFor) {
		int start=0;
		int end=array.length-1;
		
		//Cicla que no se pase
		while(start<=end) {
			
			//Mid a la mitad del arreglo
			int midPivote=(start+end)/2;
			
			
			//Debug
			System.out.println("Start: "+start);
			System.out.println("End: "+end);
			System.out.println("Mid: "+midPivote);
			System.out.println("Elemento: "+array[midPivote]);
			
			//Si es el que buscamos lo regresa
			if(array[midPivote]==lookingFor) {
				return midPivote;
				
				//Si el elemento en el indice es menor que el que buscamos, 
				//el limite inferior sube a mid+1
			}else if(array[midPivote]<lookingFor) {
				start=midPivote+1;
				
				//Si el elemento en el indice es mayor que el que buscamos, 
				//el limite superior baja a mid-1
			}else if(array[midPivote]>lookingFor){
				end=midPivote-1;
			}
					
		}
		
		return -1;
	}
}